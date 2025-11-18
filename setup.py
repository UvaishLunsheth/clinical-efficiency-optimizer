from setuptools import setup, find_packages

setup(
    name='clinical_efficiency_optimizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'streamlit', 'shap', 'xgboost','category_encoders'
    ]
)
