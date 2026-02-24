/* eslint-disable */
/* tslint:disable */
// @ts-nocheck
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

/** PayoutType */
export enum PayoutType {
  Cpa = "cpa",
  Fixed = "fixed",
  CpaFixed = "cpa_fixed",
}

/** CategoryName */
export enum CategoryName {
  Gaming = "Gaming",
  Tech = "Tech",
  Health = "Health",
  Nutrition = "Nutrition",
  Fashion = "Fashion",
  Finance = "Finance",
}

/** CategoryResp */
export interface CategoryResp {
  name: CategoryName;
  /** Id */
  id: number;
}

/** CountryOverrideCreate */
export interface CountryOverrideCreate {
  /**
   * Country Code
   * @minLength 2
   * @maxLength 2
   */
  country_code: string;
  /**
   * Cpa Amount
   * @exclusiveMin 0
   */
  cpa_amount: number;
}

/** CountryOverrideResp */
export interface CountryOverrideResp {
  /**
   * Country Code
   * @minLength 2
   * @maxLength 2
   */
  country_code: string;
  /**
   * Cpa Amount
   * @exclusiveMin 0
   */
  cpa_amount: number;
  /** Id */
  id: number;
}

/** HTTPValidationError */
export interface HTTPValidationError {
  /** Detail */
  detail?: ValidationError[];
}

/** InfluencerResp */
export interface InfluencerResp {
  /** Name */
  name: string;
  /** Id */
  id: number;
}

/** OfferCreate */
export interface OfferCreate {
  /**
   * Title
   * @maxLength 50
   */
  title: string;
  /**
   * Description
   * @maxLength 100
   */
  description: string;
  /** Categories */
  categories?: CategoryName[] | null;
  payout: PayoutCreate;
}

/** OfferResp */
export interface OfferResp {
  /**
   * Title
   * @maxLength 50
   */
  title: string;
  /**
   * Description
   * @maxLength 100
   */
  description: string;
  /** Id */
  id: number;
  /**
   * Categories
   * @default []
   */
  categories?: CategoryResp[];
  payout: PayoutResp;
}

/** OfferUpdate */
export interface OfferUpdate {
  /** Title */
  title?: string | null;
  /** Description */
  description?: string | null;
  /** Categories */
  categories?: CategoryName[] | null;
  payout?: PayoutCreate | null;
}

/** PayoutCreate */
export interface PayoutCreate {
  type: PayoutType;
  /** Cpa Amount */
  cpa_amount?: number | null;
  /** Fixed Amount */
  fixed_amount?: number | null;
  /** Influencer Id */
  influencer_id?: number | null;
  /**
   * Country Overrides
   * @default []
   */
  country_overrides?: CountryOverrideCreate[];
}

/** PayoutResp */
export interface PayoutResp {
  type: PayoutType;
  /** Cpa Amount */
  cpa_amount?: number | null;
  /** Fixed Amount */
  fixed_amount?: number | null;
  /** Id */
  id: number;
  /** Influencer Id */
  influencer_id?: number | null;
  /**
   * Country Overrides
   * @default []
   */
  country_overrides?: CountryOverrideResp[];
}

/** ValidationError */
export interface ValidationError {
  /** Location */
  loc: (string | number)[];
  /** Message */
  msg: string;
  /** Error Type */
  type: string;
}

export type QueryParamsType = Record<string | number, any>;
export type ResponseFormat = keyof Omit<Body, "body" | "bodyUsed">;

export interface FullRequestParams extends Omit<RequestInit, "body"> {
  /** set parameter to `true` for call `securityWorker` for this request */
  secure?: boolean;
  /** request path */
  path: string;
  /** content type of request body */
  type?: ContentType;
  /** query params */
  query?: QueryParamsType;
  /** format of response (i.e. response.json() -> format: "json") */
  format?: ResponseFormat;
  /** request body */
  body?: unknown;
  /** base url */
  baseUrl?: string;
  /** request cancellation token */
  cancelToken?: CancelToken;
}

export type RequestParams = Omit<
  FullRequestParams,
  "body" | "method" | "query" | "path"
>;

export interface ApiConfig<SecurityDataType = unknown> {
  baseUrl?: string;
  baseApiParams?: Omit<RequestParams, "baseUrl" | "cancelToken" | "signal">;
  securityWorker?: (
    securityData: SecurityDataType | null,
  ) => Promise<RequestParams | void> | RequestParams | void;
  customFetch?: typeof fetch;
}

export interface HttpResponse<D extends unknown, E extends unknown = unknown>
  extends Response {
  data: D;
  error: E;
}

type CancelToken = Symbol | string | number;

export enum ContentType {
  Json = "application/json",
  JsonApi = "application/vnd.api+json",
  FormData = "multipart/form-data",
  UrlEncoded = "application/x-www-form-urlencoded",
  Text = "text/plain",
}

export class HttpClient<SecurityDataType = unknown> {
  public baseUrl: string = "";
  private securityData: SecurityDataType | null = null;
  private securityWorker?: ApiConfig<SecurityDataType>["securityWorker"];
  private abortControllers = new Map<CancelToken, AbortController>();
  private customFetch = (...fetchParams: Parameters<typeof fetch>) =>
    fetch(...fetchParams);

  private baseApiParams: RequestParams = {
    credentials: "same-origin",
    headers: {},
    redirect: "follow",
    referrerPolicy: "no-referrer",
  };

  constructor(apiConfig: ApiConfig<SecurityDataType> = {}) {
    Object.assign(this, apiConfig);
  }

  public setSecurityData = (data: SecurityDataType | null) => {
    this.securityData = data;
  };

  protected encodeQueryParam(key: string, value: any) {
    const encodedKey = encodeURIComponent(key);
    return `${encodedKey}=${encodeURIComponent(typeof value === "number" ? value : `${value}`)}`;
  }

  protected addQueryParam(query: QueryParamsType, key: string) {
    return this.encodeQueryParam(key, query[key]);
  }

  protected addArrayQueryParam(query: QueryParamsType, key: string) {
    const value = query[key];
    return value.map((v: any) => this.encodeQueryParam(key, v)).join("&");
  }

  protected toQueryString(rawQuery?: QueryParamsType): string {
    const query = rawQuery || {};
    const keys = Object.keys(query).filter(
      (key) => "undefined" !== typeof query[key],
    );
    return keys
      .map((key) =>
        Array.isArray(query[key])
          ? this.addArrayQueryParam(query, key)
          : this.addQueryParam(query, key),
      )
      .join("&");
  }

  protected addQueryParams(rawQuery?: QueryParamsType): string {
    const queryString = this.toQueryString(rawQuery);
    return queryString ? `?${queryString}` : "";
  }

  private contentFormatters: Record<ContentType, (input: any) => any> = {
    [ContentType.Json]: (input: any) =>
      input !== null && (typeof input === "object" || typeof input === "string")
        ? JSON.stringify(input)
        : input,
    [ContentType.JsonApi]: (input: any) =>
      input !== null && (typeof input === "object" || typeof input === "string")
        ? JSON.stringify(input)
        : input,
    [ContentType.Text]: (input: any) =>
      input !== null && typeof input !== "string"
        ? JSON.stringify(input)
        : input,
    [ContentType.FormData]: (input: any) => {
      if (input instanceof FormData) {
        return input;
      }

      return Object.keys(input || {}).reduce((formData, key) => {
        const property = input[key];
        formData.append(
          key,
          property instanceof Blob
            ? property
            : typeof property === "object" && property !== null
              ? JSON.stringify(property)
              : `${property}`,
        );
        return formData;
      }, new FormData());
    },
    [ContentType.UrlEncoded]: (input: any) => this.toQueryString(input),
  };

  protected mergeRequestParams(
    params1: RequestParams,
    params2?: RequestParams,
  ): RequestParams {
    return {
      ...this.baseApiParams,
      ...params1,
      ...(params2 || {}),
      headers: {
        ...(this.baseApiParams.headers || {}),
        ...(params1.headers || {}),
        ...((params2 && params2.headers) || {}),
      },
    };
  }

  protected createAbortSignal = (
    cancelToken: CancelToken,
  ): AbortSignal | undefined => {
    if (this.abortControllers.has(cancelToken)) {
      const abortController = this.abortControllers.get(cancelToken);
      if (abortController) {
        return abortController.signal;
      }
      return void 0;
    }

    const abortController = new AbortController();
    this.abortControllers.set(cancelToken, abortController);
    return abortController.signal;
  };

  public abortRequest = (cancelToken: CancelToken) => {
    const abortController = this.abortControllers.get(cancelToken);

    if (abortController) {
      abortController.abort();
      this.abortControllers.delete(cancelToken);
    }
  };

  public request = async <T = any, E = any>({
    body,
    secure,
    path,
    type,
    query,
    format,
    baseUrl,
    cancelToken,
    ...params
  }: FullRequestParams): Promise<HttpResponse<T, E>> => {
    const secureParams =
      ((typeof secure === "boolean" ? secure : this.baseApiParams.secure) &&
        this.securityWorker &&
        (await this.securityWorker(this.securityData))) ||
      {};
    const requestParams = this.mergeRequestParams(params, secureParams);
    const queryString = query && this.toQueryString(query);
    const payloadFormatter = this.contentFormatters[type || ContentType.Json];
    const responseFormat = format || requestParams.format;

    return this.customFetch(
      `${baseUrl || this.baseUrl || ""}${path}${queryString ? `?${queryString}` : ""}`,
      {
        ...requestParams,
        headers: {
          ...(requestParams.headers || {}),
          ...(type && type !== ContentType.FormData
            ? { "Content-Type": type }
            : {}),
        },
        signal:
          (cancelToken
            ? this.createAbortSignal(cancelToken)
            : requestParams.signal) || null,
        body:
          typeof body === "undefined" || body === null
            ? null
            : payloadFormatter(body),
      },
    ).then(async (response) => {
      const r = response as HttpResponse<T, E>;
      r.data = null as unknown as T;
      r.error = null as unknown as E;

      const responseToParse = responseFormat ? response.clone() : response;
      const data = !responseFormat
        ? r
        : await responseToParse[responseFormat]()
            .then((data) => {
              if (r.ok) {
                r.data = data;
              } else {
                r.error = data;
              }
              return r;
            })
            .catch((e) => {
              r.error = e;
              return r;
            });

      if (cancelToken) {
        this.abortControllers.delete(cancelToken);
      }

      if (!response.ok) throw data;
      return data;
    });
  };
}

/**
 * @title Offer Manager
 * @version 0.1.0
 *
 *
 * ### Get, create, update and delete offers.
 * ### Manage custom payots for individual influencers.
 */
export class Api<
  SecurityDataType extends unknown,
> extends HttpClient<SecurityDataType> {
  api = {
    /**
     * No description
     *
     * @tags Offers
     * @name GetOffers
     * @summary Get Offers
     * @request GET:/api/offers/
     */
    getOffers: (
      query?: {
        /**
         * Offset
         * @default 0
         */
        offset?: number;
        /**
         * Limit
         * @default 20
         */
        limit?: number;
        /** Influencer Id */
        influencer_id?: number | null;
      },
      params: RequestParams = {},
    ) =>
      this.request<OfferResp[], HTTPValidationError>({
        path: `/api/offers/`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Offers
     * @name CreateOffer
     * @summary Create Offer
     * @request POST:/api/offers/
     */
    createOffer: (data: OfferCreate, params: RequestParams = {}) =>
      this.request<OfferResp, HTTPValidationError>({
        path: `/api/offers/`,
        method: "POST",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Offers
     * @name GetOffer
     * @summary Get Offer
     * @request GET:/api/offers/{offer_id}
     */
    getOffer: (offerId: number, params: RequestParams = {}) =>
      this.request<OfferResp, HTTPValidationError>({
        path: `/api/offers/${offerId}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Offers
     * @name UpdateOffer
     * @summary Update Offer
     * @request PATCH:/api/offers/{offer_id}
     */
    updateOffer: (
      offerId: number,
      data: OfferUpdate,
      params: RequestParams = {},
    ) =>
      this.request<OfferResp, HTTPValidationError>({
        path: `/api/offers/${offerId}`,
        method: "PATCH",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Offers
     * @name DeleteOffer
     * @summary Delete Offer
     * @request DELETE:/api/offers/{offer_id}
     */
    deleteOffer: (offerId: number, params: RequestParams = {}) =>
      this.request<void, HTTPValidationError>({
        path: `/api/offers/${offerId}`,
        method: "DELETE",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Payouts
     * @name GetPayouts
     * @summary Get Payouts
     * @request GET:/api/offers/{offer_id}/payouts
     */
    getPayouts: (offerId: number, params: RequestParams = {}) =>
      this.request<PayoutResp[], HTTPValidationError>({
        path: `/api/offers/${offerId}/payouts`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Payouts
     * @name CreatePayout
     * @summary Create Payout
     * @request POST:/api/offers/{offer_id}/payouts
     */
    createPayout: (
      offerId: number,
      data: PayoutCreate,
      params: RequestParams = {},
    ) =>
      this.request<PayoutResp, HTTPValidationError>({
        path: `/api/offers/${offerId}/payouts`,
        method: "POST",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Payouts
     * @name UpdatePayout
     * @summary Update Payout
     * @request PUT:/api/offers/{offer_id}/payouts/{payout_id}
     */
    updatePayout: (
      offerId: number,
      payoutId: number,
      data: PayoutCreate,
      params: RequestParams = {},
    ) =>
      this.request<PayoutResp, HTTPValidationError>({
        path: `/api/offers/${offerId}/payouts/${payoutId}`,
        method: "PUT",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Payouts
     * @name DeletePayout
     * @summary Delete Payout
     * @request DELETE:/api/offers/{offer_id}/payouts/{payout_id}
     */
    deletePayout: (
      offerId: number,
      payoutId: number,
      params: RequestParams = {},
    ) =>
      this.request<void, HTTPValidationError>({
        path: `/api/offers/${offerId}/payouts/${payoutId}`,
        method: "DELETE",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Categories
     * @name GetCategories
     * @summary Get Categories
     * @request GET:/api/categories/
     */
    getCategories: (params: RequestParams = {}) =>
      this.request<CategoryResp[], any>({
        path: `/api/categories/`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Influencers
     * @name GetInfluencers
     * @summary Get Influencers
     * @request GET:/api/influencers/
     */
    getInfluencers: (params: RequestParams = {}) =>
      this.request<InfluencerResp[], any>({
        path: `/api/influencers/`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Influencers
     * @name GetInfluencer
     * @summary Get Influencer
     * @request GET:/api/influencers/{influencer_id}
     */
    getInfluencer: (influencerId: number, params: RequestParams = {}) =>
      this.request<InfluencerResp, HTTPValidationError>({
        path: `/api/influencers/${influencerId}`,
        method: "GET",
        format: "json",
        ...params,
      }),
  };
}
