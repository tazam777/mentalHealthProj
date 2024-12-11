from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

def train_model(X, y, model=RandomForestClassifier(random_state=42)):
    """
    Train a machine learning model using the given features and target.
    
    Args:
        X (pd.DataFrame): The feature matrix.
        y (pd.Series): The target vector.
        model (sklearn estimator, optional): The model to train. Defaults to RandomForestClassifier.
        
    Returns:
        model: The trained model.
        pd.DataFrame: The test feature matrix.
        pd.Series: The test target vector.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model.fit(X_train, y_train)
    
    # Print evaluation metrics
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return model, X_test, y_test

def cross_validate_model(X, y, model=RandomForestClassifier(random_state=42), cv_folds=5):
    """
    Perform cross-validation on the given model and dataset.
    
    Args:
        X (pd.DataFrame): The feature matrix.
        y (pd.Series): The target vector.
        model (sklearn estimator, optional): The model to validate. Defaults to RandomForestClassifier.
        cv_folds (int, optional): Number of cross-validation folds. Defaults to 5.
        
    Returns:
        list: Cross-validation scores.
    """
    kf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean cross-validation accuracy: {cv_scores.mean():.2f}")
    return cv_scores
