import numpy as np

class Memory:
    def __init__(self, size=16384):
        self.memory = np.zeros(size, dtype=np.uint8)  # Memória com 16.384 bytes

    def lb(self, reg, kte):
        """Load Byte (signed): Lê um byte com sinal."""
        address = np.uint32(reg + kte)  # Calcula o endereço como uint32
        if address >= len(self.memory):
            raise ValueError("Endereço fora dos limites da memória")
        byte = np.int8(self.memory[address])  # Lê o byte como int8 (sinalizado)
        return np.int32(byte)  # Converte para int32 com extensão de sinal

    def lbu(self, reg, kte):
        """Load Byte Unsigned: Lê um byte sem sinal."""
        address = np.uint32(reg + kte)  # Calcula o endereço como uint32
        if address >= len(self.memory):
            raise ValueError("Endereço fora dos limites da memória")
        byte = self.memory[address]  # Lê o byte sem sinal
        return np.uint32(byte)  # Converte para uint32

    def lw(self, reg, kte):
        """Load Word: Lê uma palavra (4 bytes) a partir do endereço especificado."""
        address = np.uint32(reg + kte)  # Calcula o endereço como uint32
        if address % 4 != 0:
            raise ValueError("O endereço deve ser múltiplo de 4 para leitura de palavras")
        if address >= len(self.memory) or address + 4 > len(self.memory):
            raise ValueError("Endereço fora dos limites da memória")
        return int.from_bytes(self.memory[address:address+4], byteorder='little', signed=True)

    def sb(self, reg, kte, byte):
        """Store Byte: Escreve um byte na memória."""
        address = np.uint32(reg + kte)  # Calcula o endereço como uint32
        if address >= len(self.memory):
            raise ValueError("Endereço fora dos limites da memória")
        self.memory[address] = byte & 0xFF  # Garante que seja um byte (0-255)

    def sw(self, reg, kte, word):
        """Store Word: Escreve uma palavra (4 bytes) na memória."""
        address = np.uint32(reg + kte)  # Calcula o endereço como uint32
        if address % 4 != 0:
            raise ValueError("O endereço deve ser múltiplo de 4 para escrita de palavras")
        if address >= len(self.memory) or address + 4 > len(self.memory):
            raise ValueError("Endereço fora dos limites da memória")
        # Divide a palavra em 4 bytes e escreve na memória
        self.memory[address:address+4] = np.array(
            word.to_bytes(4, byteorder='little', signed=True), dtype=np.uint8
        )

# Singleton da memória compartilhada
memory_instance = Memory()
