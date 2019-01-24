# Classification-for-Credit-Applicants

We build classifier for credit applicants. This is a binary classification problem. Therefore, we build our model on Logistic Regression. In order to, apply logistic regression we need to manipulate our data.  There are some requirements to build a good model. 

* It requires categorical features to be binary. 
* Irrelevant data should be eliminated
* Attributes should not correlate with each other.
* It requires large size of data.

## Data Discovery 

In the given data we have looked at how the single attributes affect the output. In the histogram plots if different values give different outputs, it can be said that the attribute has an impact on the output and can be used in the training part creating a model. If a significant difference can’t be observed in the graph, this may indicate that the attribute has no or less effect on the output so may be discarded in the training process.
We have provided some example histograms below from the data given. In attributes: verification status, home ownership and inq_fi we have observed that the attributes have an impact on the output so we kept the attributes. In the attributes: initial list status and application type we couldn’t observe any significant effect on the data so we have decided to discard them.




