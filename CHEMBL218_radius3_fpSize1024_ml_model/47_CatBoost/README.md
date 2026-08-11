# Summary of 47_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 8
- **rsm**: 1.0
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

33.9 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.298677 | nan           |
| auc       | 0.930181 | nan           |
| f1        | 0.797225 |   0.292406    |
| accuracy  | 0.877632 |   0.497869    |
| precision | 0.969925 |   0.977924    |
| recall    | 1        |   0.000941436 |
| mcc       | 0.708488 |   0.343394    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.298677 |  nan        |
| auc       | 0.930181 |  nan        |
| f1        | 0.785515 |    0.497869 |
| accuracy  | 0.877632 |    0.497869 |
| precision | 0.815618 |    0.497869 |
| recall    | 0.757555 |    0.497869 |
| mcc       | 0.70101  |    0.497869 |


## Confusion matrix (at threshold=0.497869)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3290 |              255 |
| Labeled as 1 |              361 |             1128 |

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
