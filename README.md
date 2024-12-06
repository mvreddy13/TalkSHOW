# TalkSHOW: Generating Holistic 3D Human Motion from Speech [CVPR2023]

The official PyTorch implementation of the **CVPR2023** paper [**"Generating Holistic 3D Human Motion from Speech"**](https://arxiv.org/abs/2212.04420).

Please visit this [**webpage**](https://talkshow.is.tue.mpg.de/) for more details.

This is a forked library of the main project [TalkSHOW](https://github.com/yhw-yhw/SHOW).

## Implementation in [google Colab](https://colab.research.google.com/drive/1Q7zm4W8qHZ7AKTMvV08YSw5_JVVcwOE7?usp=sharing)
Open the above link and follow the steps in the colab notebook to implement the project.

# Implementation in Local Environment
This implementation was carried out on Ubuntu, a Linux distribution. However, you can use any other distribution of your choice.

### Getting Started

Before cloning the project into your local environment, ensure the following prerequisites are met:

- **Git**: Install Git by following [this guide](https://git-scm.com/downloads/linux).
- **Conda**: Install Conda by following [this guide](https://medium.com/@mustafa_kamal/a-step-by-step-guide-to-installing-conda-in-ubuntu-and-creating-an-environment-d4e49a73fc46).
- **Python 3.7**: Follow [this guide](https://docs.python-guide.org/starting/install3/linux/)
- And most importantly you need a **CUDA capable GPU**

### 1. Setup the environment
Clone the repo:
```bash
git clone https://github.com/mvreddy13/TalkSHOW.git
cd TalkSHOW
```
Create conda environment:
```bash
conda create --name talkshow
conda activate talkshow
```
Please install required dependecies and pytorch (v1.10.1).

    pip install -r requirements.txt
    conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge

### 2. Get Data
- Download the [pre-trained model](https://drive.google.com/file/d/1bC0ZTza8HOhLB46WOJ05sBywFvcotDZG/view) from the provided link and place it in `path-to-TalkSHOW/experiments`.
- Download [this file](https://drive.google.com/file/d/11PT4IBBbBy-r-g9YZgIyQSS1b2zuwlgX/view?usp=sharing) and place it in `path-to-TalkSHOW/visualise/smplx`.

### 3. Running the Web Application
- Since the web application is built using Streamlit, you can run it with the following command:
   ```python
   streamlit run app.py
![Homepage Image](/frontend_image.png)
