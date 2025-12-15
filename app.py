from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Datos precalculados para carga instantánea
STATIC_DATA = {
    'evaluation_metrics': {
        'purity': '0.9982725144',
        'silhouette': '0.09578003818745683',
        'calinski': '913.711950590'
    },
    'cluster_analysis': [
        {'label': -1, 'total': 1, 'malicious': 1},
        {'label': 0, 'total': 499, 'malicious': 499},
        {'label': 1, 'total': 500, 'malicious': 0}
    ],
    'features_table': [
        {'rank': 2, 'feature': 'V14', 'importance': '0.170385', 'percentage': '17.04%'},
        {'rank': 4, 'feature': 'V17', 'importance': '0.109634', 'percentage': '10.96%'},
        {'rank': 7, 'feature': 'V18', 'importance': '0.050542', 'percentage': '5.05%'},
        {'rank': 9, 'feature': 'V16', 'importance': '0.037177', 'percentage': '3.72%'},
        {'rank': 10, 'feature': 'V15', 'importance': '0.021814', 'percentage': '2.18%'}
    ],
    'total_samples': 284807,
    'fraud_samples': 492,
    'legitimate_samples': 284315
}

@app.route('/')
def index():
    """Página principal con datos estáticos precalculados"""
    return render_template('index_static.html',
                         features_table=STATIC_DATA['features_table'],
                         evaluation_metrics=STATIC_DATA['evaluation_metrics'],
                         cluster_analysis=STATIC_DATA['cluster_analysis'],
                         total_samples=STATIC_DATA['total_samples'],
                         fraud_samples=STATIC_DATA['fraud_samples'],
                         legitimate_samples=STATIC_DATA['legitimate_samples'])

@app.route('/api/stats')
def get_stats():
    """API endpoint para obtener estadísticas"""
    return jsonify({
        'total_transactions': 284807,
        'fraudulent': 492,
        'legitimate': 284315,
        'fraud_percentage': "0.172%"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
