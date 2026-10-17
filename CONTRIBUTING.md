# Guia de contribucion

## Ramas
- `main`: version estable (produccion). Solo se modifica por release o hotfix.
- `develop`: integracion del trabajo del equipo.
- `feature/<nombre>`: nueva funcionalidad (sale de develop, vuelve a develop).
- `release/<x.y.z>`: preparacion de una version (sale de develop, vuelve a main y develop).
- `hotfix/<nombre>`: correccion urgente (sale de main, vuelve a main y develop).

## Mensajes de commit (Conventional Commits)
Formato: `tipo: descripcion corta en presente`
Tipos: feat, fix, docs, refactor, test, chore.
Ejemplo: `feat: agregar descuento para clientes VIP`

## Pull Requests
1. Prueba localmente antes de subir.
2. Abre el PR hacia `develop` usando la plantilla.
3. Se necesita al menos 1 aprobacion de otro integrante.
4. Nadie aprueba su propio PR.
5. Se borra la rama despues del merge.
