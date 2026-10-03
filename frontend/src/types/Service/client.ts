

const API_URL = import.meta.env.VITE_API_URL as string;


export class ApiError extends Error {
    status: number;
    constructor(status: number, message: string) {
        super(message);
        this.status = status;
    }
}


export async function ApiRequest<T>(
    path: string, 
    options: RequestInit = {}
): Promise<T> {
    const isFormData = options.body instanceof FormData;

    const response = await fetch(`${API_URL}${path}`, {
        ...options,
        credentials: 'include',
        headers: {
            ...(!isFormData && {
                'Content-Type': 'application/json'
            }),
            ...options.headers
        }
    });

    if (response.status == 401)
        window.dispatchEvent(new CustomEvent('auth:anauthorized'));

    if (!response.ok) {
        const body = await response.json().catch(() => ({
            detail: 'Unknown error'
        }));
        throw new ApiError(response.status, body.detail ?? 'Request Failed');
    }

    if (response.status == 204)
        return undefined as T;

    return response.json() as Promise<T>

}


