# Summary of 68_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 50
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

47.4 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.467445 | nan          |
| auc       | 0.855791 | nan          |
| f1        | 0.709256 |   0.3403     |
| accuracy  | 0.786847 |   0.448435   |
| precision | 0.91716  |   0.814806   |
| recall    | 1        |   0.00377688 |
| mcc       | 0.527965 |   0.400249   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.467445 |  nan        |
| auc       | 0.855791 |  nan        |
| f1        | 0.687345 |    0.448435 |
| accuracy  | 0.786847 |    0.448435 |
| precision | 0.723238 |    0.448435 |
| recall    | 0.654846 |    0.448435 |
| mcc       | 0.527749 |    0.448435 |


## Confusion matrix (at threshold=0.448435)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2613 |              424 |
| Labeled as 1 |              584 |             1108 |

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
