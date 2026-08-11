# Summary of 56_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 20
- **max_depth**: 5
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

47.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.490398 | nan         |
| auc       | 0.831159 | nan         |
| f1        | 0.684056 |   0.403745  |
| accuracy  | 0.772468 |   0.417872  |
| precision | 0.933333 |   0.829541  |
| recall    | 1        |   0.0255435 |
| mcc       | 0.505817 |   0.403745  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.490398 |  nan        |
| auc       | 0.831159 |  nan        |
| f1        | 0.675708 |    0.417872 |
| accuracy  | 0.772468 |    0.417872 |
| precision | 0.689422 |    0.417872 |
| recall    | 0.66253  |    0.417872 |
| mcc       | 0.500806 |    0.417872 |


## Confusion matrix (at threshold=0.417872)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2532 |              505 |
| Labeled as 1 |              571 |             1121 |

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
