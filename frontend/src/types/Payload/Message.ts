


interface Info {
    full_name: string;
    user_id: number;
    profile_url: string;
    created_at: string
}


export interface MessageInfo {
    id: number;
    sender_id: number;
    receiver_id: number;
    message: string;
    image_url: string;
    message_at: string;
}


export interface MessageResponse {
    data: MessageInfo
}


export interface UsersInfo {
    data: [Info]
}


export interface GetMessagesInfo {
    data: [MessageInfo]
}


