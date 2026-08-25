# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model              |   Weight |
|:-------------------|---------:|
| 11_Xgboost         |        1 |
| 12_Xgboost         |        4 |
| 17_LightGBM        |       10 |
| 18_LightGBM        |        5 |
| 19_LightGBM        |        2 |
| 20_LightGBM        |        4 |
| 23_CatBoost        |        1 |
| 24_CatBoost        |        1 |
| 25_CatBoost        |        4 |
| 30_CatBoost        |        6 |
| 3_Default_CatBoost |        1 |
| 6_Xgboost          |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.364874 | nan         |
| auc       | 0.911898 | nan         |
| f1        | 0.797441 |   0.328178  |
| accuracy  | 0.838095 |   0.51754   |
| precision | 1        |   0.964563  |
| recall    | 1        |   0.0039724 |
| mcc       | 0.66258  |   0.328178  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.364874 |   nan       |
| auc       | 0.911898 |   nan       |
| f1        | 0.781595 |     0.51754 |
| accuracy  | 0.838095 |     0.51754 |
| precision | 0.80049  |     0.51754 |
| recall    | 0.763573 |     0.51754 |
| mcc       | 0.65354  |     0.51754 |


## Confusion matrix (at threshold=0.51754)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2476 |              326 |
| Labeled as 1 |              405 |             1308 |

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
