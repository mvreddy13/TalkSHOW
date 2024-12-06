import streamlit as st
import subprocess
import os

# Header and instructions
st.header("TalkSHOW: Generating Holistic 3D Human Motion from Speech")
st.divider()

st.image("homepage_image.jpeg", caption="Welcome to TalkSHOW", use_column_width=True)
st.markdown("Upload only **.wav** files below")

uploaded_file = st.file_uploader("Choose a .wav file", type=["wav"])

if st.button("Upload and Generate 3D Video"):
    if uploaded_file is not None:
        # Save the uploaded file locally
        wav_file_path = os.path.abspath(os.path.join("./", uploaded_file.name))
        with open(wav_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

        # Define the command to run the model
        command = [
            "python",
            "scripts/demo.py",
            "--config_file",
            "./config/LS3DCG.json",
            "--infer",
            "--audio_file",
            wav_file_path,
            "--body_model_name",
            "s2g_LS3DCG",
            "--body_model_path",
            "experiments/2022-10-19-smplx_S2G-LS3DCG/ckpt-99.pth",
            "--id",
            "0",
        ]

        # Run the command and capture output
        st.write("Processing the audio file and generating 3D mesh video...")
        try:
            result = subprocess.run(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            # Check if the command succeeded
            if result.returncode == 0:
                st.success("3D video generated successfully!")

                # Path to the output video (adjust this path as per your model's output)
                video_path = os.path.join("visualise/video/LS3DCG/TalkSHOW", f"{os.path.splitext(uploaded_file.name)[0]}.mp4")

                if os.path.exists(video_path):
                    # Display the video in Streamlit
                    st.video(video_path)

                    # Allow users to download the video
                    with open(video_path, "rb") as video_file:
                        video_bytes = video_file.read()
                        st.download_button(
                            label="Download Video",
                            data=video_bytes,
                            file_name=os.path.basename(video_path),
                            mime="video/mp4",
                        )
                else:
                    st.error("The video was not generated. Please check the model script.")
            else:
                st.error("The command failed with the following errors:")
                st.error(result.stderr)
        except Exception as e:
            st.error(f"An error occurred while running the model: {e}")
    else:
        st.warning("⚠️ Please upload a .wav file before clicking 'Upload and Generate 3D Video'.")
