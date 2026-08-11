# Summary of 55_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
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

21.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.385071 | nan         |
| auc       | 0.885417 | nan         |
| f1        | 0.728379 |   0.2765    |
| accuracy  | 0.840286 |   0.389056  |
| precision | 0.963855 |   0.914233  |
| recall    | 1        |   0.0603636 |
| mcc       | 0.6115   |   0.317497  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.385071 |  nan        |
| auc       | 0.885417 |  nan        |
| f1        | 0.720056 |    0.389056 |
| accuracy  | 0.840286 |    0.389056 |
| precision | 0.74765  |    0.389056 |
| recall    | 0.694426 |    0.389056 |
| mcc       | 0.609352 |    0.389056 |


## Confusion matrix (at threshold=0.389056)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3196 |              349 |
| Labeled as 1 |              455 |             1034 |

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
