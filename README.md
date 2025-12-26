## Nudge Engine: Stochastic Behavioral Simulation & Bayesian Analysis

### *Predicting User Decision-Making through Prospect Theory and Monte Carlo Simulations*

Este proyecto es una herramienta de **Investigación Cuantitativa de UX** diseñada para simular cómo los sesgos cognitivos —específicamente la **Aversión a la Pérdida**— impactan las tasas de conversión en un funnel digital. En lugar de depender exclusivamente de tests A/B reactivos, el **Nudge Engine** permite modelar poblaciones sintéticas y predecir resultados mediante inferencia estadística avanzada.

![Dashboard Preview](https://img.shields.io/badge/UX_Research-Quantitative-blue) ![Python](https://img.shields.io/badge/Python-3.10+-green) ![Stats](https://img.shields.io/badge/Stats-Bayesian_Inference-orange)

---

## El Problema: El coste de la incertidumbre en UX
Los tests A/B tradicionales son el estándar de oro, pero son costosos y lentos. Requieren semanas de tráfico real para alcanzar significancia estadística y conllevan el riesgo de exponer a usuarios reales a experiencias subóptimas. 

El **Nudge Engine** actúa como una capa de **validación pre-experimental**, permitiendo a los investigadores:
1.  **Priorizar Hipótesis:** Filtrar ideas de bajo impacto antes de gastar recursos de ingeniería.
2.  **Cuantificar el riesgo:** Simular escenarios de alta fricción para prever caídas en la conversión.
3.  **Aplicar rigor Bayesiano:** Obtener probabilidades de éxito accionables, superando las limitaciones de los p-values binarios.

---

## Fundamentos Científicos

### 1. Modelado de Agentes (Prospect Theory)
Cada uno de los 10,000 agentes generados posee rasgos individuales basados en la economía conductual de **Daniel Kahneman**:
*   **Coeficiente de Aversión a la Pérdida ($\lambda$):** Modelado con una distribución **Log-Normal** ($\mu=0.7, \sigma=0.2$) para reflejar que el dolor de perder es, de media, el doble que la alegría de ganar ($\lambda \approx 2.0$), pero manteniendo la varianza poblacional.
*   **Presupuesto Cognitivo:** Modelado con una **Distribución Beta**, representando la resistencia finita del usuario a la fricción y la fatiga de decisión.

### 2. Simulación Monte Carlo
En lugar de usar fórmulas deterministas, el motor utiliza **fuerza bruta estocástica**. Para cada agente, se realiza un "lanzamiento de moneda" (distribución Binomial) basado en su probabilidad individual de conversión. La agregación de estos miles de micro-experimentos genera una tasa de conversión macroscópica realista.

### 3. Inferencia Bayesiana
Sustituimos la estadística frecuentista clásica por un modelo **Beta-Bernoulli**. 
*   Comparamos las distribuciones "Posteriores" de las variantes A y B.
*   Calculamos la **Probabilidad de Superioridad**: el porcentaje de veces que la Variante B supera a la A en 4,000 universos simulados, proporcionando una métrica directa de decisión de negocio.

---

## Arquitectura Técnica (OOP)
El sistema está diseñado bajo principios de ingeniería de software, desacoplando la lógica de la presentación (Separation of Concerns):

*   **`engine.py` (Domain Layer)**: Contiene la clase `NudgeEngine`. Encapsula la lógica matemática, la generación de distribuciones y el muestreo estadístico. Es agnóstico a la interfaz.
*   **`app.py` (Presentation Layer)**: Interfaz reactiva construida con Streamlit. Se encarga de la captura de inputs, la visualización de datos con Plotly y la experiencia de usuario.

---

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/nudge-engine.git
   cd nudge-engine

  

    Instalar dependencias:
    pip install -r requirements.txt

  

Lanzar el Dashboard:

        
    streamlit run app.py

      

## Visualización de Resultados

El dashboard interactivo permite ajustar en tiempo real:

    Fricción del Funnel: Dificultad percibida del proceso.

    Potencia del Nudge: Intensidad del mensaje de aversión a la pérdida.

![img.png](assets/dashboard.png)![img_1.png](assets/graphs_detail.png)
## Limitaciones del Modelo y Validez Externa

Aunque el Nudge Engine es una herramienta potente de estimación, debe utilizarse como complemento, no sustituto, de los tests con usuarios reales.

    Reduccionismo de Variables: El modelo asume que la decisión de compra depende principalmente de la aversión a la pérdida y la carga cognitiva. En un entorno real, factores exógenos (confianza en la marca, precio, prueba social, estética) juegan un papel crucial no modelado aquí.

    Calibración de Parámetros ("Garbage In, Garbage Out"): Los parámetros base (λ≈2.0λ≈2.0) provienen de la literatura académica general. Para una precisión máxima, el modelo debería calibrarse con datos históricos del producto específico.

    Independencia de Agentes: La simulación asume que los usuarios no interactúan entre sí. No captura efectos de red, viralidad o influencia social que podrían alterar la percepción de valor.

Conclusión: Esta herramienta sirve para descartar hipótesis débiles y optimizar la estrategia de experimentación, ahorrando tiempo y presupuesto al testear solo las variantes con mayor probabilidad teórica de éxito.

Quantitative UX Researcher | Software Developer.

Desarrollado por Karim Moya. 