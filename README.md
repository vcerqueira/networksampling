## Sampling Large Scale Networks with Metropolis-Hastings Random Walk

The analysis of large-scale networks requires large working memory and powerful processors to extract useful knowledge from these data. However, not all 
companies have access to these resources, or the time needed to perform the analysis prevents them to get insight from the data in a timely manner. One possible way to circumvent this problem is to focus the analysis on a representative sample of the full network. 
The goal of sampling techniques is then to obtain a representative fragment of the network that keeps its
structural properties. The Metropolis-Hastings Random Walk (Gjoka et al., 2010) is an unbiased sampling method that provides
good results. 

#### Implementation

First, it considers a node v from the network and sets a stopping criterion. While this criterion is not met, the algorithm 

* (i) searches and randomly selects a node w, from the neighbours of v, and generates an alpha from the uniform distribution U(0,1); 
* (ii) compares alpha with Kv/Kw, where Kv and Kw represent the number of neighbours of v and w, respectively; 
* (iii) if alpha <= Kv/Kw then v is accepted and included in the sample, turning w into the reference node; otherwise, another w is picked from the neighbours of v. This "if clause" is what keeps the algorithm from biasing to nodes with a high number of neighbours.

## References

Gjoka, M., Kurant, M., Butts, C. T., and Markopoulou, A. (2010). Walking in Facebook: A Case Study of Unbiased Sampling of OSNs. In Proceedings of IEEE INFOCOM ’10, INFOCOM’10, pages 2498–2506, San Diego, California, USA. IEEE Press.