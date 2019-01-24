# Classification-for-Credit-Applicants

We build classifier for credit applicants. This is a binary classification problem. Therefore, we build our model on Logistic Regression. In order to, apply logistic regression we need to manipulate our data.  There are some requirements to build a good model. 

* It requires categorical features to be binary. 
* Irrelevant data should be eliminated
* Attributes should not correlate with each other.
* It requires large size of data.

## Data Discovery 

In the given data we have looked at how the single attributes affect the output. In the histogram plots if different values give different outputs, it can be said that the attribute has an impact on the output and can be used in the training part creating a model. If a significant difference can’t be observed in the graph, this may indicate that the attribute has no or less effect on the output so may be discarded in the training process.
We have provided some example histograms below from the data given. In attributes: verification status, home ownership and inq_fi we have observed that the attributes have an impact on the output so we kept the attributes. In the attributes: initial list status and application type we couldn’t observe any significant effect on the data so we have decided to discard them.

Indicates whether the loan is an individual application or a joint application with two co-borrowers,

![app_type](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/app_type.png)

The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER

![home_ownership](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/home_ownership1.png)

Ratio of total current balance to high credit/credit limit on all install acct, 

![initialls](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/initialls.png)

Number of personal finance inquiries,

![income](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/inq_fi1.png)


Indicates if income was verified by LC, not verified, or if the income source was verified,

![status](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/verification_status1.png)


We found out that 3 columns are almost empty through all data, so we dropped them: description of borrower (desc), annual_inc_joint and dti_joint. In the attributes emp_title, emp_length, title, dti, open_acc, total_bal_il, il_util, max_bal_bc, all_util, inq_fi, total_cu_tl and inq_last_12m we have found that there are some missing data but since the ratio of the missing data was not so high, we have filled the missing values with the mean of the attribute. By doing so, we could be able to use the data in our model without losing the general characteristic of the data.

Application type is directly related with annual_inc_joint and dti_joint. Application type can have two classes respectively, Joint App and Individual. Individuals do not have data for annual_inc_joint and dti_joint. Moreover, from the histogram above about application type, we can see that application type has small effect on classification. Therefore, it is best to drop application type for the sake of model.

Since logistic regression does not accept categorical features, we binarized the categorical features. However, some attributes have lots of classes that is not feasible to convert it to binary. So, we tried to normalize those attributes. From the attributes mp_length and term, we have removed the strings and replaced them with integers.

## Summary

We get the accuracy of %77 from Logistic regression model by applying cross validation on training data. At first, it looks good but when we analyse the ROC curve we find that our model is not classifying as expected. We get high false positive rate and true positive rates which means that for most of the cases we are giving credit to credit applicants whether they are a good applicant or not. Which indicates high recall and low precision. We get ROC under area 0.64.

![auc-roc](https://github.com/ProbisMis/Classification-for-Credit-Applicants/blob/master/Histograms/roc.png)

