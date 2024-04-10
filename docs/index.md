# ETL  - Absenteeism

## Contexto

![1712749092793](image/index/1712749092793.png)

Este projeto se trata de um processo de ***ETL (Extract, Transform e Load)*** para a área de Recursos Humanos (RH) da  **Calin Carteira Digital** . O objetivo principal é gerenciar e analisar os dados relacionados ao absenteísmo dos colaboradores. O processo de extração, transformação e carga dos dados é fundamental para garantir a integridade e a qualidade das informações utilizadas nas análises e tomadas de decisão. Ao implementar esse fluxo de ETL, busca-se otimizar a gestão de recursos humanos, identificar padrões de ausência, entender causas subjacentes e desenvolver estratégias eficazes para melhorar a produtividade e o bem-estar no ambiente de trabalho.

## Workflow

```m
mermaid
flowchart LR
	subgraph ETL [Pipeline]
		A(Multiplos Arquivos Excel) --> B[Extract: extract_from_excel]
		B[Extract: extract_from_excel] --> [Gera uma lista de Dataframes] C
		[Transformation: concat_data_frames]
		C[Transformation: concat_data_frames] --> [Gera um Dataframe consolidado] D
		[Load: Converte para Excel]
		D(Load: Converte para Excel) --> |Salva o consolidado em Excel| E(Pasta Output: Um unico arquivo Excel)
	end
```

```

```
