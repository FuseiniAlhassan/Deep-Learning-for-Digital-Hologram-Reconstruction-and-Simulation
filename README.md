# Deep-Learning-for-Digital-Hologram-Reconstruction-and-Simulation
# Abstract
This project presents an end-to-end computational imaging pipeline that unites deep learning with classical Fourier-optical simulation to reconstruct and analyze digital holograms. First, paired hologram–object datasets are organized, preprocessed, and ingested into a lightweight convolutional neural network (CNN) that learns to invert hologram intensities back to the underlying object structures. The network’s training dynamics are visualized through animated loss curves, and final predictions are refined with adaptive local thresholding to recover fine object details.
Concurrently, the repository implements analytic Fresnel-diffraction simulations: a synthetic circular aperture excites a complex field that propagates according to the transfer-function approach, yielding amplitude and phase distributions at the hologram plane. A moving-object module animates point-source motion across the field and generates corresponding dynamic holograms, saved as high-resolution GIFs.
By bridging data-driven reconstruction with rigorous wave-optical modeling, this work offers a robust platform for advancing holographic reconstruction, optical encryption, and computational microscopy. The CNN provides a fast, learned inversion that complements physically grounded propagation methods, while animations of both the optical fields and the training process deepen intuitive understanding. With modular code, clear output structuring, and extensive visualization, this toolkit equips researchers and students to explore hologram inversion, prototype novel imaging algorithms, and integrate machine learning with optical theory in graduate-level research.

# Deep Learning-Based Hologram Reconstruction and Fourier Optics Simulation

## Abstract

This project integrates deep convolutional neural networks with Fourier-optical simulations to reconstruct and visualize holographic images. First, paired hologram–object datasets are preprocessed and fed into a lightweight CNN that learns to map hologram intensities back to underlying object structures. The trained model is evaluated using local adaptive thresholding, producing binary masks that recover hidden features. In parallel, analytic simulations of Fresnel diffraction illustrate field propagation, phase encoding at the hologram plane, and dynamic moving-object hologram animations. An animated plot of CNN training loss complements the optical animations, offering insight into model convergence. By bridging deep learning and classical Fourier optics, this repository provides a comprehensive platform for advancing computational imaging and holographic reconstruction research.

---

## Project Overview

This repository contains five core components:

1. Data Preparation & Loading  
   - Organizes training and label images in a clear folder structure.  
   - Extracts ZIP archives into NumPy arrays for model input.

2. CNN-Based Hologram Reconstruction  
   - Defines a simple encoder–decoder CNN in TensorFlow/Keras.  
   - Trains the model on paired hologram–object data and saves weights.  
   - Visualizes training loss and applies local thresholding for final masks.

3. Fourier Optics Simulation  
   - Creates a circular aperture as a synthetic object field.  
   - Computes Fresnel diffraction using the transfer-function method.  
   - Visualizes amplitude and phase at the hologram plane.

4. Motion-Driven Hologram Animation  
   - Simulates a moving point-object across the grid.  
   - Animates hologram formation via Fresnel propagation.  
   - Saves results as GIF animations.

5. Training Loss Animation  
   - Generates and animates the CNN training loss curve over epochs.  
   - Provides a dynamic view of model convergence.

---

## Requirements

- Python 3.7 or higher  
- TensorFlow 2.x  
- PyTorch (optional, for data utilities)  
- NumPy  
- SciPy  
- Matplotlib  
- Pillow  
- scikit‐image  
- tqdm  

Install dependencies:

```bash
pip install numpy scipy matplotlib pillow scikit-image tqdm tensorflow torch

Concepts Illustrated
• 	Convolutional neural networks for image-to-image reconstruction
• 	Adaptive local thresholding for binary mask extraction
• 	Fresnel diffraction via Fourier-domain transfer functions
• 	Dynamic hologram simulation and GIF animation
• 	Visualization of deep learning training dynamics

Research Relevance
This project demonstrates:
• 	Integration of machine learning with classical Fourier optics
• 	An end-to-end pipeline from data loading through model training to optical simulation
• 	Interactive and static visualizations for both neural and physical optics
• 	A foundation for further research in computational imaging and holographic reconstruction

Author
Developed by Fuseini, aspiring graduate researcher in computational optics and deep learning.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute with attribution.
