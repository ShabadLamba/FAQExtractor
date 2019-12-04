export class FAQ {
  [x: string]: any;
  constructor(
    public url: string,
    // tslint:disable-next-line: variable-name
    public access_token: string,
    public fileName?: string,
    public typeOfWebsite?: number
    // tslint:disable-next-line: variable-name

  ) {
    // tslint:disable-next-line: max-line-length
    access_token = 'gAAAAABd54JjdQJuW4NCIQopW_uPmVi5Yl8hiF-et3CEflvABusLeHa9KsmONFa7XlVrFKcsPoB726W0_Q6Dur7Md4LR47UQF5XZhol64TpkW9WYpdiIBTA='
  }
}
