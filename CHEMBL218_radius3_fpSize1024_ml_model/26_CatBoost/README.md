# Summary of 26_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 4
- **rsm**: 0.9
- **loss_function**: Logloss
- **eval_metric**: Logloss
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

14.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.303213 | nan           |
| auc       | 0.927109 | nan           |
| f1        | 0.792675 |   0.286982    |
| accuracy  | 0.877235 |   0.463871    |
| precision | 0.978541 |   0.948191    |
| recall    | 1        |   0.000903409 |
| mcc       | 0.70232  |   0.463871    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.303213 |  nan        |
| auc       | 0.927109 |  nan        |
| f1        | 0.788501 |    0.463871 |
| accuracy  | 0.877235 |    0.463871 |
| precision | 0.803908 |    0.463871 |
| recall    | 0.773674 |    0.463871 |
| mcc       | 0.70232  |    0.463871 |


## Confusion matrix (at threshold=0.463871)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3264 |              281 |
| Labeled as 1 |              337 |             1152 |

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
