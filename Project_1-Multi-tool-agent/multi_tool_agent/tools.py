import psutil


def get_memory_usage() -> dict:
    """Retrieves memory statistics

    Args:
        -

    Returns:
        dict:
            - status (success or error)
            - content:
                - total (total memory; in B)
                - available (available memory; in B)
                - used (used memory; in B)
                - percent (used memory; in %)
                - free (not allocated memory; in B)
                - active (memory mapped/recently accessed by processes; in B)
                - inactive (memory not recently accessed; in B)
                - buffers (kernel-used memory to cache disk metadata; in B)
                - cached (kernel-used RAM memory to cache disk-written data; in B)
                - shared (shared memory accessible by many processes; in B)
                - slab (memory used by the kernel's internal object caches; in B)
                - wired (memory pinned in RAM by the kernel)
    """
    try:
        mem = psutil.virtual_memory()
        return mem._asdict()
    except Exception as e:
        return {'status': 'error', 'content': f'Memory stats unavailable: {e}'}

