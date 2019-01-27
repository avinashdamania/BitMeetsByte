export class User{
    first_name:string;
    last_name:string;
    age:number;
    memo:string;
    bio:string;
    skill:string;
    constructor(first_name: string, last_name:string, age:number, memo:string, bio:string, skill:string) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.age = age;
        this.memo = memo;
        this.bio = bio;
        this.skill = skill;
    }
    get_first_name():string
    {
        return this.first_name;
    }
    get_last_name():string
    {
        return this.last_name;
    }
    get_age():number
    {
        return this.age;
    }
    get_memo():string
    {
        return this.memo;
    }
    get_bio():string
    {
        return this.bio;
    }
    get_skill():string
    {
        return this.skill;
    }
}