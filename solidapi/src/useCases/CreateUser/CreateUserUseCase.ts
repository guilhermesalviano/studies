import { IUsersRespository } from "../../repostories/IUsersRepository";
import { ICreateUserRequestDTO } from "./CreateUserDTO";
import { User } from "../../entities/User";
import { IMailProvider } from "../../providers/IMailProvider";

export class CreateUserUseCase {
	/*private usersRepository: IUsersRespository;1
	constructor(usersRepository: IUsersRespository) {
		this.usersRepository = usersRepository;
    }*/
	constructor(
		private usersRepository: IUsersRespository,
		private mailProvider: IMailProvider
	) {}

	async execute(data: ICreateUserRequestDTO) {
		const userAlreadyExists = await this.usersRepository.findByEmail(
			data.email
		);

		if (userAlreadyExists) {
			throw new Error("User already exists");
		}

		const user = new User(data);

		await this.usersRepository.save(user);

		await this.mailProvider.sendMail({
			to: {
				name: data.name,
				email: data.email,
			},
			from: {
				name: "Equipe do Meu App",
				email: "equipe@meuapp.com",
			},
			subject: "Seja bem vindo a plataforma",
			body: "<p>Você já pode fazer o login em nossa plataforma.</p>",
		});
	}
}
