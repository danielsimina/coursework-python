class InformationProcessingSystem:
    def __init__(self):
        # Storage component: permanent or temporary record keeping
        self.storage = []

    def input_phase(self, raw_data):
        print(f"\n[1. INPUT] Raw data received: {raw_data}")
        return raw_data

    def processing_phase(self, raw_data):
        print(f"[2. PROCESSING] Converting raw data into useful information...")
        # Transforming raw data into structured information
        processed_info = {
            "total_items": len(raw_data),
            "formatted_items": [str(item).upper() for item in raw_data],
            "numeric_sum": sum([item for item in raw_data if isinstance(item, (int, float))])
        }
        return processed_info

    def output_phase(self, info):
        print(f"[3. OUTPUT] Presenting information to the user:")
        print(f"   -> Total Count: {info['total_items']}")
        print(f"   -> Formatted Data: {info['formatted_items']}")
        print(f"   -> Calculated Sum: {info['numeric_sum']}")

    def storage_phase(self, info):
        self.storage.append(info)
        print(f"[4. STORAGE] Saved information record. Total records in storage: {len(self.storage)}")

# --- Execution ---
computer = InformationProcessingSystem()

# Step 1: Input raw data
raw_input = ["apple", "banana", 10, 20]
data = computer.input_phase(raw_input)

# Step 2: Process data into information
information = computer.processing_phase(data)

# Step 3: Output information
computer.output_phase(information)

# Step 4: Store information
computer.storage_phase(information)