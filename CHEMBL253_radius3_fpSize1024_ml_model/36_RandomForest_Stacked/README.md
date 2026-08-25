# Summary of 36_RandomForest_Stacked

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 50
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

36.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.369408 | nan         |
| auc       | 0.909058 | nan         |
| f1        | 0.794713 |   0.393492  |
| accuracy  | 0.836988 |   0.573791  |
| precision | 0.947644 |   0.916132  |
| recall    | 1        |   0.0226508 |
| mcc       | 0.65856  |   0.393492  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.369408 |  nan        |
| auc       | 0.909058 |  nan        |
| f1        | 0.777105 |    0.573791 |
| accuracy  | 0.836988 |    0.573791 |
| precision | 0.807426 |    0.573791 |
| recall    | 0.748978 |    0.573791 |
| mcc       | 0.650037 |    0.573791 |


## Confusion matrix (at threshold=0.573791)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2496 |              306 |
| Labeled as 1 |              430 |             1283 |

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
