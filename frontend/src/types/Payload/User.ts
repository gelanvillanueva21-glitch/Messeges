

export interface LoginPayload {
    username: string;
    password: string;
}


export interface RegisterPayload extends LoginPayload{
    full_name: string;
}


export interface UserInfo {
    full_name: string;
    username: string;
    id: number;
}

