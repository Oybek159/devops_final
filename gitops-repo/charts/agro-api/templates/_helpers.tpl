{{/*
Expand the name of the chart.
*/}}
{{- define "agro-api.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "agro-api.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "agro-api.labels" -}}
app.kubernetes.io/name: {{ include "agro-api.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
