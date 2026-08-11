# Summary of 39_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 40
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

34.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.540019 | nan         |
| auc       | 0.781526 | nan         |
| f1        | 0.643929 |   0.32977   |
| accuracy  | 0.724043 |   0.505849  |
| precision | 0.881356 |   0.673618  |
| recall    | 1        |   0.0313073 |
| mcc       | 0.399285 |   0.32977   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.540019 |  nan        |
| auc       | 0.781526 |  nan        |
| f1        | 0.517917 |    0.505849 |
| accuracy  | 0.724043 |    0.505849 |
| precision | 0.69064  |    0.505849 |
| recall    | 0.414303 |    0.505849 |
| mcc       | 0.362998 |    0.505849 |


## Confusion matrix (at threshold=0.505849)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2723 |              314 |
| Labeled as 1 |              991 |              701 |

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
