# Summary of 39_RandomForest_Stacked

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 40
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

88.6 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.367406 | nan          |
| auc       | 0.909761 | nan          |
| f1        | 0.796908 |   0.398449   |
| accuracy  | 0.836766 |   0.54852    |
| precision | 0.953608 |   0.933993   |
| recall    | 1        |   0.00790742 |
| mcc       | 0.663085 |   0.44152    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.367406 |   nan       |
| auc       | 0.909761 |   nan       |
| f1        | 0.779803 |     0.54852 |
| accuracy  | 0.836766 |     0.54852 |
| precision | 0.798654 |     0.54852 |
| recall    | 0.761821 |     0.54852 |
| mcc       | 0.65069  |     0.54852 |


## Confusion matrix (at threshold=0.54852)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2473 |              329 |
| Labeled as 1 |              408 |             1305 |

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
