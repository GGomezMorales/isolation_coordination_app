######################## 1ª ETAPA: builder ########################
FROM ubuntu:24.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Capa de dependencias (aprovecha la caché de Docker)
WORKDIR /install
COPY requirements.txt .
RUN pip3 install --no-cache-dir --prefix=/python -r requirements.txt

# Copiamos el código fuente
WORKDIR /src

######################## 2ª ETAPA: runtime ########################
FROM ubuntu:24.04

# Copiamos solo Python + dependencias + código
COPY --from=builder /python /python
COPY --from=builder /src /app

# Ajustamos variables de entorno para que Python funcione desde /python
ENV PATH="/python/bin:${PATH}" \
    PYTHONPATH="/python/lib/python3.12/site-packages" \
    PYTHONUNBUFFERED=1

# Crea un usuario no-root por seguridad
RUN useradd -u 1001 -ms /bin/bash appuser
USER 1001

WORKDIR /app
EXPOSE 5000
CMD ["python3", "-m", "app.main"]
