# Summary of 32_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
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

36.7 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.467624 | nan          |
| auc       | 0.858362 | nan          |
| f1        | 0.731876 |   0.393145   |
| accuracy  | 0.784718 |   0.446403   |
| precision | 0.92268  |   0.828209   |
| recall    | 1        |   0.00607949 |
| mcc       | 0.551017 |   0.39916    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.467624 |  nan        |
| auc       | 0.858362 |  nan        |
| f1        | 0.713443 |    0.446403 |
| accuracy  | 0.784718 |    0.446403 |
| precision | 0.720667 |    0.446403 |
| recall    | 0.706363 |    0.446403 |
| mcc       | 0.541139 |    0.446403 |


## Confusion matrix (at threshold=0.446403)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2333 |              469 |
| Labeled as 1 |              503 |             1210 |

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
