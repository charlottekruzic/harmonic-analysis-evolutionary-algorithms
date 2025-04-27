# Harmonies Unveiled: Harmonic analysis by artificial evolution

## 🔎 Overview
This project explores an alternative approach to Fourier transform-based harmonic analysis using artificial evolution algorithms. The goal is to iteratively determine the parameters (amplitude, frequency, and phase) of sinusoids that compose a complex signal.

## ❓ Problem statement
While Fourier transform analysis can reveal frequency information in complex signals, it has limitations when trying to extract specific phase information for individual sinusoids in a multi-sinusoidal signal. This project implements a "sines peeling" technique using evolutionary algorithms to overcome these limitations.

## 〰️ Signal composition
The test signal is composed of 100 sinusoids with the following parameters:
- **Amplitudes**: The 100 prime numbers starting from 31 (in decreasing order: 601, 599, 593, etc.)
- **Frequencies**: The 100 prime numbers starting from 1000 (in increasing order: 1009, 1013, 1019, etc.)
- **Phases**: 2π divided by the first 100 prime numbers (2, 3, 5, 7, etc.)
> For example:
> - First sinusoid: _601 * sin(1009x + 6.28/2)_
> - Second sinusoid: _599 * sin(1013x + 6.28/3)_
> - Third sinusoid: _593 * sin(1019x + 6.28/5)_

## 📝 Methodology
1. Generate a composite signal by summing 100 sinusoids with the parameters defined above
2. Sample the signal with 8192 points in the interval [0, 7]
3. Use an evolutionary algorithm to find the first sinusoid with the largest amplitude
4. Remove the approximated sinusoid from the signal
5. Repeat the process to find subsequent sinusoids

## ⚙️ Implementation
The project uses EASEA (EAsy Specification of Evolutionary Algorithms) for implementing the evolutionary algorithm. Key components include:
- **Population size**: 2000
- **Number of generations**: 190
- **Mutation probability**: 20%
- **Crossover probability**: 100%
- **Selection operator**: Tournament of size 2
- **Random seed**: 4 (for reproducibility)

## 📊 Results
The evolutionary approach successfully identified:
- First sinusoid: _602.213013 * sin(1009.061279 * x + 6.28/2.136420)_ 
    > Expected: _601 * sin(1009 * x + 6.28/2)_
- Second sinusoid: _596.213013 * sin(1013.017273 * x + 6.28/2.658169)_
    > Expected: _599 * sin(1013 * x + 6.28/3)_
- Third sinusoid: _585.213013 * sin(1018.856140 * x + 6.28/3.156052)_
    > Expected: _593 * sin(1019 * x + 6.28/5)_

However, accuracy deteriorated significantly after the third sinusoid.

## 🚫 Limitations
- Noise accumulation from imperfect approximations
- Difficulty in accurately determining parameters for lower amplitude sinusoids
- Phase and amplitude correlation issues

## 🛠️ Usage
To run the project:
1. Install EASEA platform from https://easea.unistra.fr/
2. Use the seed value 4 for reproducibility
3. Run the .ez file with EASEA

## 🎓 Academic context
This project was developed during the first year of the Master’s program in Data Science and Complex Systems at the University of Strasbourg.

## 📝 Documentation
For more detailed information about this project, the full [project report](./resources/project-report-fr.pdf) (in french) and the [original assignment specifications](./resources/project-assignment.pdf) are available in the `./resources` directory. These documents provide in-depth explanations of the theoretical background, methodological approach, and comprehensive analysis of results.

## 👷‍♂️ Contributors
- Zoé Marquis
- Charlotte Kruzic