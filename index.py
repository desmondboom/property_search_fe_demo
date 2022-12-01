import streamlit as st
import requests


def request(keyword: str, limit: int):
    url = f"http://localhost:5000/search?key=%s&limit=%d" % (keyword, limit)
    data = requests.get(url)
    return data.json()


def gallery_display(_list: list):
    st.markdown("### Results")
    st.image(
        image=list(
            map(lambda detail: detail['media']['mainImage']['templatedUrl'], _list)
        ),
        caption=list(
            map(lambda detail: detail['address']['display']['fullAddress'], _list)
        ),
    )


if __name__ == '__main__':
    st.title("Property Search AI Enhancement")
    st.markdown("### Search The Property")

    search_text: str = st.text_input(
        label="keywords", max_chars=20, placeholder="apartment", help="keywords of search"
    )
    search_limit: int = st.slider(
        label="limit", min_value=1, max_value=10, value=4, help="how many result to return"
    )
    clicked = st.button(label="Search", type="primary")

    if clicked:
        property_list = request(search_text, search_limit)
        gallery_display(property_list)

    introduction = """
    ### Project Introduction
    Imagine that:

    * You come across a dreamy house but you cannot find it online.
    * You have one photo and you want to search exactly with it.
    * You want to find the property with some features.

    We want to enhance the search function on main page, 
    allowing our users to find the property they want 
    based on the description of appearance with only  **a few words** or simply one **photo**.

    What we gonna do is to set up a neural search engine using one multi-mode pre-trained model 
    [*CLIP*](https://openai.com/blog/clip/). 
    We encode the images of the properties and search the best fit property with one sentence or photo.
    """
    st.markdown(introduction)
