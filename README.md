# actividad-integradora-abril-2

- Análisis de caso
* Una empresa inspirada en Spotify mantiene una plataforma web para reproducir contenido digital y administrar perfiles de usuario. En las últimas semanas, el equipo ha detectado varios problemas:

- Las nuevas versiones no siempre funcionan igual en todos los equipos.
- No existe un proceso automático para validar cambios antes de integrarlos.
- La aplicación y algunos servicios auxiliares se ejecutan manualmente en cada entorno.
- No hay una forma clara de preparar el despliegue futuro en la nube.
- La dirección técnica solicita una propuesta rápida y funcional para estandarizar el entorno, separar responsabilidades en servicios, automatizar verificaciones y preparar la base para despliegues posteriores.



- Análisis del caso
* La plataforma presenta un déficit en la estandarización de entornos, lo que genera el clásico conflicto de "en mi máquina sí funciona" al intentar desplegar nuevas versiones. La ejecución manual de servicios auxiliares incrementa el riesgo operativo y dificulta la escalabilidad, mientras que la ausencia de un pipeline de validación impide detectar fallos antes de la integración. Esta falta de estructura técnica no solo compromete la estabilidad actual del servicio de streaming, sino que actúa como un cuello de botella para la migración hacia una arquitectura de nube (AWS) más robusta y eficiente.  





- Problemas a resolver 
+ Para estabilizar la plataforma inspirada en Spotify, se deben atacar los siguientes puntos críticos:
* Disparidad de Entornos: Diferencias en las configuraciones locales de los desarrolladores que causan fallos en producción.
* Ausencia de Automatización (CI): Dependencia de revisiones manuales, lo que permite la entrada de bugs y archivos faltantes en las ramas principales.
* Gestión Manual de Servicios: La falta de orquestación (Docker Compose) para la aplicación y sus auxiliares genera lentitud en el despliegue y errores humanos.
* Falta de Visibilidad en Infraestructura: Inexistencia de un plan de monitoreo y despliegue escalable que soporte el crecimiento de usuarios y datos (S3/EC2).   

