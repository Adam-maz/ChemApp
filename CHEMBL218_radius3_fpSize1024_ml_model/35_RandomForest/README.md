# Summary of 35_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 50
- **max_depth**: 4
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

17.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.431186 | nan         |
| auc       | 0.845677 | nan         |
| f1        | 0.685734 |   0.274087  |
| accuracy  | 0.821216 |   0.34975   |
| precision | 0.961373 |   0.813255  |
| recall    | 1        |   0.0965741 |
| mcc       | 0.559045 |   0.34975   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.431186 |   nan       |
| auc       | 0.845677 |   nan       |
| f1        | 0.681077 |     0.34975 |
| accuracy  | 0.821216 |     0.34975 |
| precision | 0.72093  |     0.34975 |
| recall    | 0.6454   |     0.34975 |
| mcc       | 0.559045 |     0.34975 |


## Confusion matrix (at threshold=0.34975)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3173 |              372 |
| Labeled as 1 |              528 |              961 |

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
