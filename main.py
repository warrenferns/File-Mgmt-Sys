import streamlit as st
from azure.storage.blob import BlobClient, ContainerClient

def upload():
    st.title("Cloud Computing Lab - Mini Project")
    #Connection String to Azure Storage
    connection_string = '#'
    uploaded_file = st.file_uploader('',type= '.pdf',accept_multiple_files=False)
    if st.button("Upload"):
        blob_client = BlobClient.from_connection_string(connection_string, container_name="photos", blob_name=uploaded_file.name)
        blob_client.upload_blob(uploaded_file.read())
        st.sidebar.info("Successfully Uploaded")

def download():
    st.title("Cloud Computing Lab - Mini Project")
    #Connection String to Azure Storage
    connection_string = '#'
    container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name="photos")
    blobs = container_client.list_blobs()
    for blob in blobs:
        st.markdown(blob.name)
        if st.button("Download", key=blob.name):
            blob_client = BlobClient.from_connection_string(connection_string, container_name="photos", blob_name=blob.name)
            bytes = blob_client.download_blob().readall()
            st.download_button('Download file', bytes)

if __name__ == '__main__':
    nav = st.sidebar.radio("", ["Upload", "Download"])
    if nav == "Upload":
        upload()
    if nav == "Download":
        download()