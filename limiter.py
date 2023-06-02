import numpy as np

def limiter(signal, threshold):
    """
    Лимитирует звуковой сигнал на выходе с пороговым значением.
    :param signal: Входной звуковой сигнал (одномерный массив NumPy)
    :param threshold: Пороговое значение (в децибелах)
    :return: Лимитированный звуковой сигнал
    """
    # Вычисляем максимальное значение амплитуды
    max_amp = np.max(np.abs(signal))
    
    # Вычисляем коэффициент сжатия на основе порогового значения
    compression_ratio = 10**(threshold / 20)  # Переводим из децибелов в линейную шкалу
    
    # Применяем лимитирование сжатием амплитуды сигнала
    limited_signal = signal / max_amp  # Нормализуем амплитуды
    limited_signal = np.tanh(limited_signal * compression_ratio)  # Применяем сжатие (гиперболический тангенс)
    
    # Масштабируем сигнал обратно к исходной амплитуде
    limited_signal = limited_signal * max_amp
    
    return limited_signal

# Пример использования
input_signal = np.array([0.2, 0.5, 0.8, 1.0, 0.3, 0.6, 0.9])
threshold_db = -10  # Пороговое значение в децибелах
limited_signal = limiter(input_signal, threshold_db)
print(limited_signal)
