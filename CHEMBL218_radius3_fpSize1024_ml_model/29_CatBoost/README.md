# Summary of 29_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 7
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

21.5 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.299765 | nan          |
| auc       | 0.929482 | nan          |
| f1        | 0.797566 |   0.331423   |
| accuracy  | 0.878824 |   0.500439   |
| precision | 0.972678 |   0.967204   |
| recall    | 1        |   0.00053934 |
| mcc       | 0.709425 |   0.364853   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.299765 |  nan        |
| auc       | 0.929482 |  nan        |
| f1        | 0.787604 |    0.500439 |
| accuracy  | 0.878824 |    0.500439 |
| precision | 0.817787 |    0.500439 |
| recall    | 0.75957  |    0.500439 |
| mcc       | 0.703935 |    0.500439 |


## Confusion matrix (at threshold=0.500439)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3293 |              252 |
| Labeled as 1 |              358 |             1131 |

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
