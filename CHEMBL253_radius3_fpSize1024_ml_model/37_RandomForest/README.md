# Summary of 37_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
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

39.1 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.491738 | nan          |
| auc       | 0.828023 | nan          |
| f1        | 0.676799 |   0.31806    |
| accuracy  | 0.767604 |   0.45742    |
| precision | 0.933333 |   0.834841   |
| recall    | 1        |   0.00924534 |
| mcc       | 0.481058 |   0.417433   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.491738 |   nan       |
| auc       | 0.828023 |   nan       |
| f1        | 0.643529 |     0.45742 |
| accuracy  | 0.767604 |     0.45742 |
| precision | 0.713156 |     0.45742 |
| recall    | 0.586288 |     0.45742 |
| mcc       | 0.478564 |     0.45742 |


## Confusion matrix (at threshold=0.45742)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2638 |              399 |
| Labeled as 1 |              700 |              992 |

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
