# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 30
- **max_depth**: 4
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

34.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.515309 |  nan        |
| auc       | 0.802949 |  nan        |
| f1        | 0.655052 |    0.322488 |
| accuracy  | 0.744766 |    0.443628 |
| precision | 0.932432 |    0.78786  |
| recall    | 1        |    0.021051 |
| mcc       | 0.439325 |    0.407484 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.515309 |  nan        |
| auc       | 0.802949 |  nan        |
| f1        | 0.620082 |    0.443628 |
| accuracy  | 0.744766 |    0.443628 |
| precision | 0.6633   |    0.443628 |
| recall    | 0.582151 |    0.443628 |
| mcc       | 0.431212 |    0.443628 |


## Confusion matrix (at threshold=0.443628)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2537 |              500 |
| Labeled as 1 |              707 |              985 |

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
