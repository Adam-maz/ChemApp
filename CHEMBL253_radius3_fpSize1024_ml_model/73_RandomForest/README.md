# Summary of 73_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.9
- **min_samples_split**: 40
- **max_depth**: 6
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

47.4 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.47766  | nan          |
| auc       | 0.84308  | nan          |
| f1        | 0.692624 |   0.383786   |
| accuracy  | 0.774794 |   0.420281   |
| precision | 0.92623  |   0.820132   |
| recall    | 1        |   0.00822662 |
| mcc       | 0.509485 |   0.414024   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.47766  |  nan        |
| auc       | 0.84308  |  nan        |
| f1        | 0.683507 |    0.420281 |
| accuracy  | 0.774794 |    0.420281 |
| precision | 0.687388 |    0.420281 |
| recall    | 0.679669 |    0.420281 |
| mcc       | 0.508744 |    0.420281 |


## Confusion matrix (at threshold=0.420281)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2514 |              523 |
| Labeled as 1 |              542 |             1150 |

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
