# ACM Research Coding Challenge (Fall 2020)

## Solution by Eric Zhang
I thought of this admittedly naive clustering algorithm while reading the problem, and a quick search showed that it was most similar in logic to DBSCAN. 

The idea is that all points within a certain, user-specified range of a point should be counted in the same cluster. If a point is in two different clusters, then those clusters must be the same cluster. By this method, we can chain an entire cluster together.

My algorithm is a little brute-forcey and has room for improvement, for example caching the distances between points. The steps are as follows:  
1. Input all verticies.
2. Assign IDs to all of the verticies.
3. Use a union find to join points less than a certain distance apart
4. Count the number of clusters containing over 5% of the total number of points  

The only import I used was math, for square rooting.  

One potential shortcoming of this method is that the distance tolerance has to be determined by the user and is not automatic. This could potentially be mitigated by taking a quartile of the set of all distances. 

In the current implementation, a distance tolerance of 0.2 - 1.0 (inclusive) will give an answer of 2 clusters. A tolerance of 0.1 splits the top cluster at around the $X=4.7$ mark, giving 3 clusters.

# Original Problem Readme 

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.
