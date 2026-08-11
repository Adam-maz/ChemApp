# Summary of 70_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
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

39.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.466431 | nan         |
| auc       | 0.854887 | nan         |
| f1        | 0.712915 |   0.367659  |
| accuracy  | 0.789596 |   0.438141  |
| precision | 0.92     |   0.86574   |
| recall    | 1        |   0.0122883 |
| mcc       | 0.540543 |   0.400405  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.466431 |  nan        |
| auc       | 0.854887 |  nan        |
| f1        | 0.695812 |    0.438141 |
| accuracy  | 0.789596 |    0.438141 |
| precision | 0.720709 |    0.438141 |
| recall    | 0.672577 |    0.438141 |
| mcc       | 0.536031 |    0.438141 |


## Confusion matrix (at threshold=0.438141)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2596 |              441 |
| Labeled as 1 |              554 |             1138 |

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
