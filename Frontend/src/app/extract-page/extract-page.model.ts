export class FAQ {
  [x: string]: any;
  constructor(
    public url: string,
    public fileName?: string,
    public typeOfWebsite?: number
  ) { }
}
