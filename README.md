# Spam Message Classifier

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using TF-IDF text vectorization and the Multinomial Naive Bayes algorithm.

## Project Overview

Spam messages can contain unwanted promotions, misleading offers, or suspicious links. This project uses natural language processing (NLP) techniques and machine learning to identify whether a message is spam or a normal message.

## Features

- Cleans and prepares SMS message data.
- Converts text into numerical features using TF-IDF.
- Trains a Multinomial Naive Bayes classifier.
- Evaluates the model using accuracy, precision, recall, F1-score, and a confusion matrix.
- Tests the trained model on sample messages.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Dataset

The project uses an SMS spam dataset containing message text and labels:

- `ham`: normal message
- `spam`: spam message

The dataset was cleaned before training. The model used a stratified train-test split, with 80% of the data for training and 20% for testing.

> Add the dataset source here if required. Do not upload a dataset unless you have permission to share it.

## Project Workflow

1. Load and inspect the dataset.
2. Clean the data and retain the label and message columns.
3. Explore the distribution of ham and spam messages.
4. Split the data into training and testing sets.
5. Convert text into TF-IDF features using unigrams and bigrams.
6. Train a Multinomial Naive Bayes model.
7. Compare different `alpha` values and select `alpha=0.1` based on the current test results.
8. Evaluate the model and test sample messages.

## Model Performance

The selected model (`MultinomialNB(alpha=0.1)`) achieved the following results on the test set:

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.99 | 0.98 |
| Recall | 1.00 | 0.92 |
| F1-score | 0.99 | 0.95 |
| Support | 903 | 131 |

- **Accuracy:** 98.84%
- **Test samples:** 1,034
- **Spam messages correctly identified:** 121 out of 131
- **Spam messages missed:** 10
- **Normal messages incorrectly flagged as spam:** 2

These results describe the current test split and may differ on other data.

## Installation and Usage

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd SpamMessageClassifier
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository URL.

### 2. Create and activate a virtual environment (optional)

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn jupyter
```

### 4. Add the dataset

Place the dataset CSV file in the project folder and update the notebook's file path if needed. The notebook may require the dataset's actual filename and column names.

### 5. Run the notebook

```bash
jupyter notebook
```

Open the project's `.ipynb` notebook and run its cells in order.

## Example Predictions

| Sample message | Predicted class |
|---|---|
| Congratulations! You have won a free prize. Claim now! | SPAM |
| Hey, are we meeting today? | HAM |
| URGENT! You have won a cash reward. Call now! | SPAM |
| Please send me the class notes. | HAM |

These are example predictions, not a guarantee that every similar message will be classified correctly.

## Limitations and Future Improvements

- Some spam messages may still be classified as ham.
- Evaluate on additional, unseen messages to check generalization.
- Try other text-classification algorithms and compare their results.
- Consider a simple user interface for entering and classifying messages.

## Conclusion

This project demonstrates how TF-IDF and Multinomial Naive Bayes can be used for SMS spam classification. The model achieved 98.84% accuracy on the current test set, with a spam recall of approximately 92%, while leaving room for further improvement.


