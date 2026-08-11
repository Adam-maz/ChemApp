# Summary of 34_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 30
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

33.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.53785  | nan         |
| auc       | 0.780288 | nan         |
| f1        | 0.641364 |   0.332741  |
| accuracy  | 0.72933  |   0.512806  |
| precision | 0.906667 |   0.719473  |
| recall    | 1        |   0.0474789 |
| mcc       | 0.398221 |   0.332741  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.53785  |  nan        |
| auc       | 0.780288 |  nan        |
| f1        | 0.518797 |    0.512806 |
| accuracy  | 0.72933  |    0.512806 |
| precision | 0.71281  |    0.512806 |
| recall    | 0.407801 |    0.512806 |
| mcc       | 0.375736 |    0.512806 |


## Confusion matrix (at threshold=0.512806)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2759 |              278 |
| Labeled as 1 |             1002 |              690 |

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
