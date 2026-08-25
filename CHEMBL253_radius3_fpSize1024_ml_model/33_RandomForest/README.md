# Summary of 33_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 1.0
- **min_samples_split**: 20
- **max_depth**: 3
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

28.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.545443 | nan         |
| auc       | 0.780598 | nan         |
| f1        | 0.665205 |   0.305496  |
| accuracy  | 0.715393 |   0.512644  |
| precision | 0.919463 |   0.706716  |
| recall    | 1        |   0.0331678 |
| mcc       | 0.412814 |   0.305496  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.545443 |  nan        |
| auc       | 0.780598 |  nan        |
| f1        | 0.569802 |    0.512644 |
| accuracy  | 0.715393 |    0.512644 |
| precision | 0.667975 |    0.512644 |
| recall    | 0.496789 |    0.512644 |
| mcc       | 0.37286  |    0.512644 |


## Confusion matrix (at threshold=0.512644)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2379 |              423 |
| Labeled as 1 |              862 |              851 |

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
