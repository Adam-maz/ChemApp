# Summary of 74_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.8
- **min_samples_split**: 40
- **max_depth**: 7
- **eval_metric_name**: logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **stratify**: True
 - **k_folds**: 5
 - **shuffle**: True
 - **random_seed**: 42

## Optimized metric
logloss

## Training time

22.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.37361  | nan         |
| auc       | 0.89714  | nan         |
| f1        | 0.738966 |   0.266305  |
| accuracy  | 0.843067 |   0.370681  |
| precision | 0.962406 |   0.929107  |
| recall    | 1        |   0.0096467 |
| mcc       | 0.622027 |   0.266305  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.37361  |  nan        |
| auc       | 0.89714  |  nan        |
| f1        | 0.729637 |    0.370681 |
| accuracy  | 0.843067 |    0.370681 |
| precision | 0.743894 |    0.370681 |
| recall    | 0.715917 |    0.370681 |
| mcc       | 0.619369 |    0.370681 |


## Confusion matrix (at threshold=0.370681)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3178 |              367 |
| Labeled as 1 |              423 |             1066 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
