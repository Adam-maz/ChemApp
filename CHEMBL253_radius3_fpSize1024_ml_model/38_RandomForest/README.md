# Summary of 38_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.8
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

44.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.47756  | nan         |
| auc       | 0.844505 | nan         |
| f1        | 0.698522 |   0.364041  |
| accuracy  | 0.777754 |   0.462627  |
| precision | 0.92623  |   0.830094  |
| recall    | 1        |   0.0077022 |
| mcc       | 0.514357 |   0.396861  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.47756  |  nan        |
| auc       | 0.844505 |  nan        |
| f1        | 0.659098 |    0.462627 |
| accuracy  | 0.777754 |    0.462627 |
| precision | 0.73041  |    0.462627 |
| recall    | 0.600473 |    0.462627 |
| mcc       | 0.5018   |    0.462627 |


## Confusion matrix (at threshold=0.462627)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2662 |              375 |
| Labeled as 1 |              676 |             1016 |

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
