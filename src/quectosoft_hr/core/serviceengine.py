class ServiceEngine:
    @staticmethod
    def build_llm_instruction(service, payload, context):
        return f"Service={service} payload={payload} context={context}"
    @staticmethod
    def build_service_context(service, payload, context):
        return {"service": service, "payload": payload, "context": context}
